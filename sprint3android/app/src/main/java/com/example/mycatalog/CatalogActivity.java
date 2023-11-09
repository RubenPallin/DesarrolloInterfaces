package com.example.mycatalog;

import androidx.appcompat.app.AppCompatActivity;
import androidx.fragment.app.Fragment;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;

public class CatalogActivity extends Fragment {

    // Constructor público vacío requerido para la inicialización del fragmento.
    public CatalogActivity() {
    }

    // Método onCreateView se llama para crear la vista del fragmento.
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflar el layout para este fragmento y asignar a rootView.
        View rootView = inflater.inflate(R.layout.activity_catalog, container, false);

        // Encontrar el botón en la vista inflada del fragmento.
        Button buttonOne = rootView.findViewById(R.id.buttonToDetail);

        // Establecer un escuchador de clics en el botón.
        buttonOne.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Usar getActivity() para obtener el contexto de la actividad contenedora.
                Intent intent = new Intent(getActivity(), DetailActivity.class);
                // Iniciar DetailActivity desde el fragmento.
                startActivity(intent);
            }
        });

        // Devolver la vista inflada.
        return rootView;
    }
}