package main

type StoreItem struct {
	Val       string
	Timestamp int
}
type TimeMap struct {
	Store map[string][]StoreItem
}

func Constructor() TimeMap {
	return TimeMap{
		Store: map[string][]StoreItem{},
	}
}

func (this *TimeMap) Set(key string, value string, timestamp int) {
	this.Store[key] = append(this.Store[key], StoreItem{value, timestamp})
}

func (this *TimeMap) Get(key string, timestamp int) string {
	values, exists := this.Store[key]
	if !exists || len(values) == 0 {
		return ""
	}

	var res string
	l, r := 0, len(values)-1

	for l <= r {
		mid := (l + r) / 2
		if values[mid].Timestamp <= timestamp {
			res = values[mid].Val
			l = mid + 1
		} else {
			r = mid - 1
		}
	}

	return res
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Set(key,value,timestamp);
 * param_2 := obj.Get(key,timestamp);
 */
