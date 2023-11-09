package com.example.mycatalog;

import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;


import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.ActionBarDrawerToggle;
import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;
import androidx.core.view.GravityCompat;
import androidx.drawerlayout.widget.DrawerLayout;
import androidx.fragment.app.Fragment;

import com.google.android.material.navigation.NavigationView;


public class MainActivity extends AppCompatActivity {
    private ActionBarDrawerToggle toggle;
    private DrawerLayout drawerLayout;
    private NavigationView navView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Toolbar toolbar = findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        drawerLayout = findViewById(R.id.drawerLayout);
        navView = findViewById(R.id.navView);

        toggle = new ActionBarDrawerToggle(this, drawerLayout, toolbar, R.string.navigation_drawer_open, R.string.navigation_drawer_close);
        drawerLayout.addDrawerListener(toggle);
        toggle.syncState();

        navView.setNavigationItemSelectedListener(this::onNavigationItemSelected);

    }

    // Este método maneja la selección de ítems en la NavigationView.

    public boolean onNavigationItemSelected(@NonNull MenuItem item) {
        // Inicialmente establece el fragmento a mostrar como nulo.
        Fragment fragment = null;

        // Obtiene el ID del ítem seleccionado.
        int id = item.getItemId();

        // Crea una instancia del fragmento correspondiente al ítem seleccionado.
        if (id == R.id.nav_fragment1) {
            fragment = new AboutFragment();
        } else if (id == R.id.nav_fragment2) {
            fragment = new CatalogActivity();
        }

        // Reemplaza el contenido del contenedor con el fragmento seleccionado.
        if (fragment != null) {
            getSupportFragmentManager().beginTransaction()
                    .replace(R.id.fragment_container, fragment)
                    .commit();
        }

        // Cierra el menú deslizante una vez que se ha realizado una selección.
        DrawerLayout drawer = findViewById(R.id.drawerLayout);
        drawer.closeDrawer(GravityCompat.START);
        // Devuelve verdadero para indicar que el evento de selección fue manejado.
        return true;
    }
    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Manejar los clics en el ícono del menú en la barra de herramientas
        if (toggle.onOptionsItemSelected(item)) {
            return true;
        }
        return super.onOptionsItemSelected(item);
    }
    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        getMenuInflater().inflate(R.menu.nav_header_menu, menu);
        return true;
    }
}