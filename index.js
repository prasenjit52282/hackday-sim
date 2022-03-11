const buildLegendDiv = () => {
    return `
    <div style="padding:10px;font-size:16px">
      <table>
          <thead>
              <h3>Legends</h3>
          </thead>
          <tbody>
              <tr>
                  <td><i style="color:grey;" class="fas fa-circle"></i></td>
                  <td>Stopping</td>
              </tr>
              <tr>
                  <td><i style="color:green;" class="fas fa-circle"></i></td>
                  <td>Good Road</td>
              </tr>
              <tr>
                  <td><i style="color:orange;" class="fas fa-circle"></i></td>
                  <td>Medium Road</td>
              </tr>
              <tr>
                  <td><i style="color:red;" class="fas fa-circle"></i></td>
                  <td>Bad Road</td>
              </tr>
          </tbody>
      </table>
      </div>
      `;
  };

map = initialize({ lat: 23.68852, long: 87.2564 }, document.getElementById("map-canvas"));

const legendDiv=document.getElementById("legend")
legendDiv.innerHTML = buildLegendDiv();
map.controls[google.maps.ControlPosition.LEFT_BOTTOM].push(legendDiv);


const moveMarker = (map, marker, lat, lon) => {
    marker.setPosition(new google.maps.LatLng(lat, lon));
    map.panTo(new google.maps.LatLng(lat, lon));
};

const autoRefresh = (coords, map) => {
    let marker = new google.maps.Marker({
        map: map,
    });
    let labelmap={"-1":"grey","1":"green","2":"orange","3":"red",};
    let tpoints=0;

    coords.forEach((segment, i) => {

        const label = segment[0]
        const points = segment[1]

        let route;

        route = new google.maps.Polyline({
            path: [],
            geodesic: true,
            strokeColor: labelmap[label.toString()], // according to label
            strokeOpacity: 0.7,
            strokeWeight: 7,
            editable: false,
            map: map,
        });

        
        

        points.forEach((obj, j) => {
            let timer = setTimeout(
                (coords) => {
                    route.getPath().push(new google.maps.LatLng(coords.lat, coords.lng));
                    moveMarker(map, marker, coords.lat, coords.lng);
                },
                25 * tpoints,
                obj
            );
            tpoints+=1
        })

    })
};



autoRefresh(data,map);