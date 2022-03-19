let subs;
let canvas;
let myMap;
let countries;
const mappa = new Mappa("Leaflet");
const options = {
  lat: 0,
  lng: 0,
  zoom: 4,
  style: "http://{s}.tile.osm.org/{z}/{x}/{y}.png",
};
function preload() {
  subs = loadTable("subs.csv");
  countries = loadJSON("countries.json");
}
function setup() {
  for(let row of subs.rows){
    console.log(`${row.get('country_id')} ${row.get('country_name')} ${row.get('views')}`);
  }
  canvas = createCanvas(800, 600);
  myMap = mappa.tileMap(options);
  myMap.overlay(canvas);
}

function draw() {
  // for(let row of subs.rows){
  //   console.log(`${row.get('country_id')} ${row.get('country_name')} ${row.get('views')}`);
  //   let country = row.get('country_id').toLowerCase();
  //   let latLon = countries[country];
  //   if(latLon){
  //     let {lat,lon} = latLon;
  //     const pix = myMap.latLngToPixel(lat,lon);
  //     fill(255,0,200);
  //     ellipse(100,100,50,50);
  //   }
  // }
  //background(mouseX%mouseY);
}
