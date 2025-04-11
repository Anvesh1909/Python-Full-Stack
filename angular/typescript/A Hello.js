console.log("Hello world!");
var a = 10;
console.log("a = " + a);
var pid = 1001;
var pname = "mobile1";
var price = 9999.99;
console.log(pid, pname, price);
var productDetails = [1001, "mobile1", 9999.99];
console.log(productDetails);
function hello() {
    console.log("Hello function in type script");
}
hello();
function empFunction(eid, ename, esal) {
    console.log("\n\nWith formal parameters\n");
    console.log("eid : ", eid);
    console.log("ename : ", ename);
    console.log("esal : ", esal);
}
empFunction(101, "Anvesh", 20000.00);
function empFunction2(eid, ename, esal) {
    if (eid === void 0) { eid = 101; }
    if (ename === void 0) { ename = "Anvesh"; }
    if (esal === void 0) { esal = 5000; }
    console.log("\n\nWith default parameters\n");
    console.log("eid : ", eid);
    console.log("ename : ", ename);
    console.log("esal : ", esal);
}
empFunction2();
function Add(a, b) {
    console.log("\n\nAdd function\n");
    return a + b;
}
console.log(Add(10, 20));
function Add1() {
    var argv = [];
    for (var _i = 0; _i < arguments.length; _i++) {
        argv[_i] = arguments[_i];
    }
    console.log("\n\n rest parameter add operation \n");
    var sum = 0;
    for (var i = 0; i < argv.length; i++) {
        sum += argv[i];
    }
    return sum;
}
console.log(Add1(1, 2, 3, 4, 5));
var Student = /** @class */ (function () {
    function Student() {
        console.log("\n\nNon parameterized construstor");
    }
    return Student;
}());
var s1 = new Student();
var Student2 = /** @class */ (function () {
    function Student2() {
        console.log("\n\nparameterized construstor");
    }
    return Student2;
}());
var s2 = new Student2();
