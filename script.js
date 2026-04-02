fetch('data/weather.json')
  .then(res => res.json())
  .then(data => {
    document.getElementById("temp").innerText = data.temp + "°C";
    document.getElementById("humidity").innerText = data.humidity + "%";
    document.getElementById("heat").innerText = data.heat_index + "°C";
    document.getElementById("status").innerText = data.status;

    if (data.heat_index > 40) {
      document.body.style.backgroundColor = "#ff4d4d";
    }
  });
