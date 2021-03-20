package structure

type StockData struct {
	Children []Stock `json:"children"`
}

type Stock struct {
	StockId   string         `json:"id"`
	MarketCap string         `json:"$marketcap"`
	Board     string         `json:"$board"`
	Sector    interface{}    `json:"$sector"`
	PriceData StockPriceData `json:"data"`
}

type StockPriceData struct {
	Price                string `json:"price"`
	PriceChange          string `json:"pricechange"`
	PriceChangeInPercent string `json:"pricechangepct"`
	TradedVolume         string `json:"$area"`
}
