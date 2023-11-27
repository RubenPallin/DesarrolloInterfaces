package com.example.myothercatalog;

import android.app.Activity;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.bumptech.glide.Glide;

// ViewHolder que representa la vista de un elemento en el RecyclerView
public class ProtagonistasViewHolder extends RecyclerView.ViewHolder {

    private final TextView textView;   // Vista de texto para el nombre del protagonista
    private final ImageView imageView;  // Vista de imagen para la imagen del protagonista

    // Constructor que inicializa las vistas en el ViewHolder
    public ProtagonistasViewHolder(@NonNull View itemView) {
        super(itemView);
        textView = (TextView) itemView.findViewById(R.id.prota_name_text_view);
        imageView = (ImageView) itemView.findViewById(R.id.prota_image_view);
    }

    // Método para mostrar los datos de un protagonista en las vistas
    public void showData(ProtagonistasData data, Activity activity){
        textView.setText(data.getName());  // Establece el nombre del protagonista en la vista de texto
        // Utiliza la biblioteca Glide para cargar la imagen del protagonista en la vista de imagen
        Glide.with(itemView.getContext())
                .load(data.getImageUrl())
                .into(imageView);
    }
}
