package main

import (
	"context"
	"fmt"
	"log"
	"stockgrepper/mongoConnHelper"
	"stockgrepper/stockData"
	"stockgrepper/structure"
	"time"

	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/bson/primitive"
	"go.mongodb.org/mongo-driver/mongo"
)

const DB = "stocks"
const Col = "klse"
const Holdings = "myHoldings"

var mappingInMongo = make(map[string]primitive.ObjectID)
var myHoldings = make(map[string]bool)
var stocks *[]structure.Stock

func main() {
	client, err := mongoConnHelper.GetMongoClient()
	if err != nil {
		log.Fatal(err)
	}
	ctx, _ := context.WithTimeout(context.Background(), 10*time.Second)
	defer client.Disconnect(ctx)

	err = initMyHoldings(client)
	if err != nil {
		log.Fatal(err)
	}
	err = initMappings(client)
	if err != nil {
		log.Fatal(err)
	}
	for i := 1; i < 2; i++ {
		stocks = stockData.GetStockData(myHoldings)
		for _, v := range *stocks {
			UpdateStock(client, v)
		}
	}
	fmt.Println("Done")
}

func CreateStock(client *mongo.Client, stock structure.Stock) error {
	collection := client.Database(DB).Collection(Col)
	_, err := collection.InsertOne(context.TODO(), stock)
	if err != nil {
		return err
	}
	return nil
}

func CreateStocks(client *mongo.Client, stocks []structure.Stock) error {
	stocksToInsert := make([]interface{}, len(stocks))
	for i, v := range stocks {
		stocksToInsert[i] = v
	}

	collection := client.Database(DB).Collection(Col)
	_, err := collection.InsertMany(context.TODO(), stocksToInsert)
	if err != nil {
		return err
	}
	return nil
}

func UpdateStock(client *mongo.Client, newData structure.Stock) {
	collection := client.Database(DB).Collection(Col)
	result, err := collection.ReplaceOne(
		context.TODO(),
		bson.M{"_id": mappingInMongo[newData.StockId]},
		newData,
	)
	if err != nil {
		log.Fatal(err)
	}
	if result.ModifiedCount == 0 {
		err = CreateStock(client, newData)
		if err != nil {
			log.Fatal(err)
		}
	}
}

func initMappings(client *mongo.Client) error {
	collection := client.Database(DB).Collection(Col)
	ctx := context.TODO()
	cursor, err := collection.Find(ctx, bson.M{})
	if err != nil {
		return err
	}
	var stocks []struct {
		Id      primitive.ObjectID `bson:"_id,omitempty"`
		Stockid string             `bson:"stockid"`
	}
	if err = cursor.All(ctx, &stocks); err != nil {
		return err
	}
	for _, v := range stocks {
		mappingInMongo[v.Stockid] = v.Id
	}
	return nil
}

func findDocument(client *mongo.Client, id primitive.ObjectID) error {
	collection := client.Database(DB).Collection(Col)
	var stock structure.Stock
	var err error
	ctx := context.TODO()
	err = collection.FindOne(ctx, bson.M{"_id": id}).Decode(&stock)
	if err != nil {
		return err
	}
	fmt.Println(stock)
	return nil
}

func initMyHoldings(client *mongo.Client) error {
	collection := client.Database(DB).Collection(Holdings)
	var holdings struct {
		Id     primitive.ObjectID `bson:"_id"`
		Stocks map[string]bool    `bson:"stocks"`
	}
	err := collection.FindOne(context.TODO(), bson.M{}).Decode(&holdings)
	if err != nil {
		return err
	}
	myHoldings = holdings.Stocks
	return nil
}
