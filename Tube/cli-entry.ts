import * as fs from "fs";


// 读取输入文件
const inputFile = process.argv[2]; // 获取传入的 JSON 文件
if (!inputFile) {
    console.error("Error: No input file provided.");
    process.exit(1);
}

// 解析 JSON 文件
let inputData;
try {
    const fileContent = fs.readFileSync(inputFile, "utf-8");
    inputData = JSON.parse(fileContent);
} catch (error) {
    console.error("Error reading input file:", error);
    process.exit(1);
}

// 生成 GCode 的函数
function planWind(data: any): string {
    let gcode = "";
    gcode += "; GCode for Tube Winding\n";
    gcode += `; Inner Diameter: ${data.inner_diameter}mm\n`;
    gcode += `; Wall Thickness: ${data.wall_thickness}mm\n`;
    gcode += `; Length: ${data.length}mm\n\n`;

    gcode += "G0 X0 Y0 Z0\n"; // 初始位置
    gcode += `G92 X${data.inner_diameter} Y${data.wall_thickness} Z${data.length}\n`;
    
    // 模拟 GCode 层
    for (let i = 1; i <= 3; i++) {
        gcode += `; Layer ${i}\n`;
        gcode += `G1 X${data.inner_diameter + i} Y${data.wall_thickness + i} Z${data.length + i} F${data.feed_rate}\n`;
    }

    return gcode;
}

// 生成 GCode
const gcodeOutput = planWind(inputData);

// 保存 GCode 到文件
fs.writeFileSync("output.gcode", gcodeOutput);
console.log("✅ GCode has been generated: output.gcode");
