package com.example.myothercatalog;

import android.content.Intent;
import android.os.Bundle;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import com.bumptech.glide.Glide;

// Actividad para mostrar detalles de un protagonista seleccionado
public class DetailActivity extends AppCompatActivity {

    // Constantes para identificar los extras en el intent
    public static final String TITLE = "TITLE";
    public static final String URL = "URL";
    public static final String DESCRIPTION = "DESCRIPTION";

    private String url;           // URL de la imagen del protagonista
    private String description;   // Descripción del protagonista
    private String title;         // Nombre del protagonista

    // Método llamado cuando se crea la actividad
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        // Establece el diseño de la actividad desde activity_detail.xml
        setContentView(R.layout.activity_detail);

        // Inicializa las vistas de la actividad
        ImageView image = findViewById(R.id.imageview_detail_activity);
        TextView title_detail = findViewById(R.id.textTitle);
        TextView description_detail = findViewById(R.id.descriptionText);

        // Obtiene el intent que inició esta actividad
        Intent intent = getIntent();

        // Obtiene los extras del intent (nombre, descripción, URL)
        title = intent.getStringExtra(TITLE);
        description = intent.getStringExtra(DESCRIPTION);
        url = intent.getStringExtra(URL);

        // Utiliza Glide para cargar la imagen del protagonista en la vista de imagen
        Glide.with(DetailActivity.this).load(url).into(image);
        // Establece el nombre y la descripción del protagonista en las vistas correspondientes
        title_detail.setText(title);
        description_detail.setText(description);
    }
}
