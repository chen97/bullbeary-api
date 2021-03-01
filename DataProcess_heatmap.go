package main

import (
	"fmt"
	"io/ioutil"
	"net/http"

	"context"
	"log"
	"time"

	"github.com/bitly/go-simplejson"
	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
)

func main() {
	client, err := mongo.NewClient(options.Client().ApplyURI("mongodb://localhost:27017/"))
	if err != nil {
		log.Fatal(err)
	}
	ctx, _ := context.WithTimeout(context.Background(), 10*time.Second)
	err = client.Connect(ctx)
	if err != nil {
		log.Fatal(err)
	}
	defer client.Disconnect(ctx)

	quickstartDatabase := client.Database("Bullbeary")
	StocksCollection := quickstartDatabase.Collection("Stocks")

	resp, err := http.Get("https://www.bursamarketplace.com/bin/json/stockheatmap.json")
	if err != nil {
		panic(err)
	}
	data, err := ioutil.ReadAll(resp.Body)

	js, err := simplejson.NewJson([]byte(data))
	if err != nil {
		fmt.Print("NewJson error:", err.Error())
		return
	}

	// 获取 answerInfos 节点
	stocks := js.Get("children")

	// answerInfos 下面是一个数组
	// rows是 []interface{}，类型
	stock, err := stocks.Array()
	if err != nil {
		fmt.Print("Get answerInfos error:", err.Error())
		return
	}

	// 打印answerInfos下数组长度，这里只有1个节点，所以是1
	//fmt.Printf("answerInfos size:%d \n", len(stock))

	// row是interface{}类型
	for index := range stock {
		// rows是数组，所以需要再获取一下节点
		node := stocks.GetIndex(index)

		id := node.Get("id").MustString()
		cashtag := node.Get("data").Get("cashtag").MustString()
		name := node.Get("name").MustString()
		stockPrice := node.Get("data").Get("price").MustString()
		stockFullName := node.Get("data").Get("companyname").MustString()
		price_change_rm := node.Get("data").Get("pricechange").MustString()
		price_change_pct := node.Get("data").Get("pricechangepct").MustString()
		volume := node.Get("$active").MustString()
		marketcap := node.Get("$marketcap").MustString()
		board := node.Get("$board").MustString()
		sector := node.Get("$sector").MustString()
		is_shariah := node.Get("$shariah").MustString()

		// Add stock
		/*
			fmt.Printf("StockName:%s, StockPrice:%s \n", name, stockPrice)
			StocksResult, err := StocksCollection.InsertOne(ctx, bson.D{
				{Key: "id", Value: id},
				{Key: "cashtag", Value: cashtag},
				{Key: "name", Value: name},
				{Key: "full_name", Value: stockFullName},
				{Key: "stock_price", Value: stockPrice},
				{Key: "price_change_rm", Value: price_change_rm},
				{Key: "price_change_pct", Value: price_change_pct},
				{Key: "volume", Value: volume},
				{Key: "marketcap", Value: marketcap},
				{Key: "board", Value: board},
				{Key: "sector", Value: sector},
				{Key: "is_shariah", Value: is_shariah},
			})
			if err != nil {
				log.Fatal(err)
			}
			fmt.Printf("Inserted %v documents into episode collection!\n", (StocksResult))
		*/

		// Update stock
		fmt.Printf("StockName:%s, StockPrice:%s \n", name, stockPrice)
		StocksResult, err := StocksCollection.UpdateOne(ctx,
			bson.M{
				"id": id},
			bson.M{
				"$set": bson.D{
					{Key: "cashtag", Value: cashtag},
					{Key: "name", Value: name},
					{Key: "full_name", Value: stockFullName},
					{Key: "stock_price", Value: stockPrice},
					{Key: "price_change_rm", Value: price_change_rm},
					{Key: "price_change_pct", Value: price_change_pct},
					{Key: "volume", Value: volume},
					{Key: "marketcap", Value: marketcap},
					{Key: "board", Value: board},
					{Key: "sector", Value: sectorName(sector)},
					{Key: "is_shariah", Value: is_shariah},
				},
			},
		)
		if err != nil {
			log.Fatal(err)
		}
		fmt.Printf("Inserted %v documents into episode collection!\n", (StocksResult))
	}
}

func sectorName(name string) string {
	switch name {
	case "50":
		return "Energy"
	case "51":
		return "Basic Materials"
	case "52":
		return "Industrials"
	case "53":
		return "Consumer Cyclicals"
	case "54":
		return "Consumer Non-Cyclicals"
	case "55":
		return "Financials"
	case "56":
		return "Healthcare"
	case "57":
		return "Technology"
	case "58":
		return "Telecommunication Services"
	case "59":
		return "Utilities"
	}
	return "Null"
}
