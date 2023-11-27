package com.example.myothercatalog;

import org.json.JSONException;
import org.json.JSONObject;

// Clase que representa los datos de un protagonista
public class ProtagonistasData {
    private String name;         // Nombre del protagonista
    private String imageUrl;     // URL de la imagen del protagonista
    private String description;   // Descripción del protagonista

    // Constructor que recibe un objeto JSONObject y lo utiliza para inicializar los atributos
    public ProtagonistasData(JSONObject json){
        try{
            this.name = json.getString("name");
            this.imageUrl = json.getString("image_url");
            this.description = json.getString("description");
        } catch(JSONException e){
            e.printStackTrace();
        }
    }

    // Método para obtener el nombre del protagonista
    public String getName() {
        return name;
    }

    // Método para obtener la URL de la imagen del protagonista
    public String getImageUrl() {
        return imageUrl;
    }

    // Método para obtener la descripción del protagonista
    public String getDescription() {
        return description;
    }
}