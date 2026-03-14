const fs = require("fs");
const fetch = require("node-fetch");

const sheetURL =
"https://docs.google.com/spreadsheets/d/1PlqIBtGVKHCQIoDk4gAbIOIpRh_-bEGRXmexvaT5sos/gviz/tq";

function slugify(text){
return text
.toLowerCase()
.normalize("NFD")
.replace(/[\u0300-\u036f]/g,"")
.replace(/ /g,"-");
}

async function generate(){

const res = await fetch(sheetURL);
const text = await res.text();

const json = JSON.parse(
text.substring(text.indexOf("{"), text.lastIndexOf("}") + 1)
);

const rows = json.table.rows;

if(!fs.existsSync("termek")){
fs.mkdirSync("termek");
}

rows.forEach(r=>{

if(!r.c) return;

const name = r.c[0]?.v || "";
const images = r.c[2]?.v || "";
const description = r.c[3]?.v || "";

const slug = slugify(name);

const firstImage = images.split("|")[0];

const html = `
<!DOCTYPE html>
<html lang="hu">
<head>

<meta charset="UTF-8">
<title>${name} – Ruhatárház</title>

<meta property="og:type" content="product">
<meta property="og:title" content="${name} – Ruhatárház">
<meta property="og:description" content="${description}">
<meta property="og:image" content="https://ruhatarhaz.hu/images/${firstImage}">
<meta property="og:url" content="https://ruhatarhaz.hu/termek/${slug}">

<meta http-equiv="refresh" content="0; url=/product.html?slug=${slug}">

</head>
<body></body>
</html>
`;

fs.writeFileSync(`termek/${slug}.html`, html);

});

console.log("SEO termékoldalak generálva.");

}

generate();
