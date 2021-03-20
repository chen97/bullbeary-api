package mongoConnHelper

import (
	"context"

	"sync"
	"time"

	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
)

const uri = "mongodb+srv://kahhwa:SiIrgKfGdwEsENgh@cluster0.weni0.mongodb.net/test"

var mongoOnce sync.Once

func GetMongoClient() (*mongo.Client, error) {

	var instanceError error
	var clientInstance *mongo.Client
	mongoOnce.Do(func() {
		client, err := mongo.NewClient(options.Client().ApplyURI(uri))
		if err != nil {
			instanceError = err
		}
		ctx, _ := context.WithTimeout(context.Background(), 10*time.Second)
		err = client.Connect(ctx)
		if err != nil {
			instanceError = err
		}
		clientInstance = client
	})
	return clientInstance, instanceError
}
