package main

import "fmt"

// Pair 結構用來儲存 (key, value) 鍵值對
type Pair struct {
	key   int
	value int
}

// MyHashMap 結構，bucket 為一個 Pair 的二維 slice
type MyHashMap struct {
	size   int
	bucket [][]Pair
}

// Constructor 建構子：初始化 MyHashMap
func Constructor() MyHashMap {
	size := 100001 // 可根據需求調整，這裡用 100001 作為 bucket 大小
	buckets := make([][]Pair, size)
	return MyHashMap{size: size, bucket: buckets}
}

// hash 方法：根據 key 取餘數得到 bucket 索引
func (this *MyHashMap) hash(key int) int {
	return key % this.size
}

// Put 方法：插入或更新 (key, value) 鍵值對
func (this *MyHashMap) Put(key int, value int) {
	hashKey := this.hash(key)
	found := false
	// 遍歷該 bucket 中所有 Pair
	for i, kv := range this.bucket[hashKey] {
		if key == kv.key {
			// 若發現相同的 key，則更新 value
			this.bucket[hashKey][i].value = value
			found = true
			break
		}
	}
	// 若 bucket 中沒有該 key，則 append 一個新的 Pair
	if !found {
		this.bucket[hashKey] = append(this.bucket[hashKey], Pair{key: key, value: value})
	}
}

// Get 方法：根據 key 回傳對應的 value，找不到則回傳 -1
func (this *MyHashMap) Get(key int) int {
	hashKey := this.hash(key)
	for _, kv := range this.bucket[hashKey] {
		if key == kv.key {
			return kv.value
		}
	}
	return -1
}

// Remove 方法：根據 key 刪除對應的鍵值對
func (this *MyHashMap) Remove(key int) {
	hashKey := this.hash(key)
	for i, kv := range this.bucket[hashKey] {
		if kv.key == key {
			// 使用 slice 的切片操作刪除該元素
			this.bucket[hashKey] = append(this.bucket[hashKey][:i], this.bucket[hashKey][i+1:]...)
			break
		}
	}
}

func main() {
	obj := Constructor()
	obj.Put(1, 10)
	fmt.Println(obj.Get(1)) // 輸出 10
	obj.Remove(1)
	fmt.Println(obj.Get(1)) // 輸出 -1 (找不到)
}
