// 빈 JSON 객체 생성
const myDict = {};

// 값 삽입
myDict["apple"] = 3;
myDict["banana"] = 5;

// 값 조회 --> 3
console.log(myDict["apple"]);

// 키 존재 여부 확인 --> true
console.log("banana" in myDict);

// 값 수정
myDict["apple"] = 10;

// 값 삭제
delete myDict["banana"];

// Map 객체 생성
const myDict = new Map();

// 값 삽입
myDict.set("apple", 3);
myDict.set("banana", 5);

// 값 조회 --> 3
console.log(myDict.get("apple"));

// 키 존재 여부 확인 --> true
console.log(myDict.has("banana"));

// 값 수정
myDict.set("apple", 10);

// 값 삭제
myDict.delete("banana");