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


public class MainActivity extends AppCompatActivity implements Select_Listener{

    @Override
    protected void onCreate(Bundle saveInstanceState) {
        super.onCreate(saveInstanceState);
        setContentView(R.layout.activity_main);
        RecyclerView recyclerView = findViewById(R.id.recycler_view);
        Activity activity = this;
        JsonArrayRequest request = new JsonArrayRequest(
                Request.Method.GET,
                "https://raw.githubusercontent.com/RubenPallin/DesarrolloInterfaces/main/recursos/catalog.json",
                null,
                new Response.Listener<JSONArray>() {
                    @Override
                    public void onResponse(JSONArray response) {
                        List<ProtagonistasData> allTheProtas = new ArrayList<>();
                        for (int i = 0; i < response.length(); i++){
                            try{
                                JSONObject protas = response.getJSONObject(i);
                                ProtagonistasData data = new ProtagonistasData(protas);
                                allTheProtas.add(data);
                            }catch (JSONException e){
                                e.printStackTrace();
                            }
                        }
                        ProtagonistasRecyclerViewAdapter adapter = new ProtagonistasRecyclerViewAdapter(allTheProtas, activity, MainActivity.this );
                        recyclerView.setAdapter(adapter);
                        recyclerView.setLayoutManager(new LinearLayoutManager(activity));
                    }
                },new Response.ErrorListener() {

            @Override
            public void onErrorResponse(VolleyError error) {
                Toast.makeText(activity, error.getMessage(), Toast.LENGTH_SHORT).show();
            }
        });
        RequestQueue cola = Volley.newRequestQueue(this);
        cola.add(request);
    }

    @Override
    public void onItemClick(ProtagonistasData allTheProtas) {
        Intent intent = new Intent(MainActivity.this, DetailActivity.class);
        startActivity(intent);
    }
}
