class RecentCounter{
    constructor(){
        this.arr = [];
    }    
}

RecentCounter.prototype.ping = function(t) {
    this.arr.push(t)
    while(this.arr[0] + 3000 < t){
        this.arr.shift();
    }
    return this.arr.length;
};

var obj = new RecentCounter()
var pings = [1,100,3001,3002];
var expected = [1, 2, 3, 3];
for (var i = 0; i < pings.length; i++)
{
    var elem = pings[i];
    param_1 = obj.ping(elem);
    console.log(elem, param_1, expected[i]);
}