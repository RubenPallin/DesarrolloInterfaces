package com.example.myothercatalog;


import android.app.Activity;
import android.os.Bundle;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonArrayRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.List;
import android.content.Intent;


// Declaración de la clase MainActivity que extiende AppCompatActivity e implementa la interfaz Select_Listener
public class MainActivity extends AppCompatActivity implements Select_Listener {

    // Método llamado cuando se crea la actividad
    @Override
    protected void onCreate(Bundle saveInstanceState) {
        super.onCreate(saveInstanceState);
        // Establece el diseño de la actividad desde activity_main.xml
        setContentView(R.layout.activity_main);

        // Inicializa el RecyclerView para mostrar la lista de elementos
        RecyclerView recyclerView = findViewById(R.id.recycler_view);
        // Almacena la referencia a la actividad actual
        Activity activity = this;

        // Realiza una solicitud JSON usando Volley para obtener datos del catálogo
        JsonArrayRequest request = new JsonArrayRequest(
                Request.Method.GET,
                "https://raw.githubusercontent.com/RubenPallin/DesarrolloInterfaces/main/recursos/catalog.json",
                null,
                new Response.Listener<JSONArray>() {
                    // Callback para manejar la respuesta exitosa
                    @Override
                    public void onResponse(JSONArray response) {
                        // Lista para almacenar objetos ProtagonistasData
                        List<ProtagonistasData> allTheProtas = new ArrayList<>();

                        // Itera sobre el JSONArray para crear objetos ProtagonistasData
                        for (int i = 0; i < response.length(); i++){
                            try{
                                JSONObject protas = response.getJSONObject(i);
                                ProtagonistasData data = new ProtagonistasData(protas);
                                allTheProtas.add(data);
                            } catch (JSONException e){
                                e.printStackTrace();
                            }
                        }

                        // Configura el RecyclerView con el adaptador y el administrador de diseño
                        ProtagonistasRecyclerViewAdapter adapter = new ProtagonistasRecyclerViewAdapter(allTheProtas, activity, MainActivity.this);
                        recyclerView.setAdapter(adapter);
                        recyclerView.setLayoutManager(new LinearLayoutManager(activity));
                    }
                }, new Response.ErrorListener() {
            // Callback para manejar errores en la respuesta
            @Override
            public void onErrorResponse(VolleyError error) {
                // Muestra un Toast con el mensaje de error
                Toast.makeText(activity, error.getMessage(), Toast.LENGTH_SHORT).show();
            }
        });

        // Cola de solicitudes Volley
        RequestQueue cola = Volley.newRequestQueue(this);
        // Agrega la solicitud a la cola
        cola.add(request);
    }

    // Método de la interfaz Select_Listener, activado cuando se hace clic en un elemento del RecyclerView
    @Override
    public void onItemClick(ProtagonistasData allTheProtas) {
        // Crea un intent para abrir la actividad DetailActivity
        Intent intent = new Intent(MainActivity.this, DetailActivity.class);
        // Obtiene información del elemento seleccionado y la agrega como extras en el intent
        String title = allTheProtas.getName();
        String url = allTheProtas.getImageUrl();
        String description = allTheProtas.getDescription();
        intent.putExtra(DetailActivity.TITLE, title);
        intent.putExtra(DetailActivity.URL, url);
        intent.putExtra(DetailActivity.DESCRIPTION, description);
        // Inicia la actividad DetailActivity con el intent
        startActivity(intent);
    }
}
