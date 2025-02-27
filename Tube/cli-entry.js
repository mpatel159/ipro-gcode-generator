"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var fs = require("fs");
// 读取输入文件
var inputFile = process.argv[2]; // 获取传入的 JSON 文件
if (!inputFile) {
    console.error("Error: No input file provided.");
    process.exit(1);
}
// 解析 JSON 文件
var inputData;
try {
    var fileContent = fs.readFileSync(inputFile, "utf-8");
    inputData = JSON.parse(fileContent);
}
catch (error) {
    console.error("Error reading input file:", error);
    process.exit(1);
}
// 生成 GCode 的函数
function planWind(data) {
    var gcode = "";
    gcode += "; GCode for Tube Winding\n";
    gcode += "; Inner Diameter: ".concat(data.inner_diameter, "mm\n");
    gcode += "; Wall Thickness: ".concat(data.wall_thickness, "mm\n");
    gcode += "; Length: ".concat(data.length, "mm\n\n");
    gcode += "G0 X0 Y0 Z0\n"; // 初始位置
    gcode += "G92 X".concat(data.inner_diameter, " Y").concat(data.wall_thickness, " Z").concat(data.length, "\n");
    // 模拟 GCode 层
    for (var i = 1; i <= 3; i++) {
        gcode += "; Layer ".concat(i, "\n");
        gcode += "G1 X".concat(data.inner_diameter + i, " Y").concat(data.wall_thickness + i, " Z").concat(data.length + i, " F").concat(data.feed_rate, "\n");
    }
    return gcode;
}
// 生成 GCode
var gcodeOutput = planWind(inputData);
// 保存 GCode 到文件
fs.writeFileSync("output.gcode", gcodeOutput);
console.log("✅ GCode has been generated: output.gcode");
