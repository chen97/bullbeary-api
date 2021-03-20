package stockData

import (
	"encoding/json"
	"log"
	"net/http"
	"stockgrepper/structure"
)

func GetStockData(myHoldings map[string]bool) *[]structure.Stock {
	stocks := make([]structure.Stock, len(myHoldings))
	var err error
	var response *http.Response
	var responseObject structure.StockData
	const stockDataEndPoint string = "https://www.bursamarketplace.com/bin/json/stockheatmap.json"
	response, err = http.Get(stockDataEndPoint)
	if err != nil {
		log.Fatal(err)
	}
	err = json.NewDecoder(response.Body).Decode(&responseObject)
	if err != nil {
		log.Fatal(err)
	}
	var count int = 0
	for _, v := range responseObject.Children {
		if myHoldings[v.StockId] {
			stocks[count] = v
			count++
		}
	}
	return &stocks
}
