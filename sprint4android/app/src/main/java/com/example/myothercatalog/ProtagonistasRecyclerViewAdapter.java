package com.example.myothercatalog;

import android.app.Activity;
import android.content.Intent;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.List;


// Adaptador para el RecyclerView que muestra la lista de protagonistas
public class ProtagonistasRecyclerViewAdapter extends RecyclerView.Adapter<ProtagonistasViewHolder> {

    private List<ProtagonistasData> allTheData;     // Lista de datos de protagonistas
    private Activity activity;                      // Referencia a la actividad que contiene el RecyclerView
    private Select_Listener select_listener;        // Interfaz para manejar eventos de clic en el RecyclerView

    // Constructor que recibe la lista de datos, la actividad y la interfaz Select_Listener
    public ProtagonistasRecyclerViewAdapter(List<ProtagonistasData> allTheData, Activity activity, Select_Listener listener) {
        this.allTheData = allTheData;
        this.activity = activity;
        this.select_listener = listener;
    }

    // Método llamado cuando se necesita crear un nuevo ViewHolder
    @NonNull
    @Override
    public ProtagonistasViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        // Infla la vista del ViewHolder desde el diseño prota_view_holder.xml
        View view = LayoutInflater.from(parent.getContext())
                .inflate(R.layout.protagonistas_view_holder, parent, false);
        // Retorna un nuevo objeto ProtagonistasViewHolder con la vista inflada
        return new ProtagonistasViewHolder(view);
    }

    // Método llamado para actualizar la información en un ViewHolder específico
    @Override
    public void onBindViewHolder(@NonNull ProtagonistasViewHolder holder, int position) {
        // Obtiene los datos del protagonista en la posición especificada
        ProtagonistasData dataInPositionToBeRendered = allTheData.get(position);
        // Muestra los datos en el ViewHolder utilizando el método showData
        holder.showData(dataInPositionToBeRendered, activity);

        // Configura un OnClickListener en la vista del ViewHolder para manejar clics
        holder.itemView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                // Llama al método onItemClick de la interfaz Select_Listener al hacer clic en un elemento
                select_listener.onItemClick(dataInPositionToBeRendered);
            }
        });
    }

    // Método que devuelve la cantidad total de elementos en la lista de datos
    @Override
    public int getItemCount() {
        return allTheData.size();
    }
}