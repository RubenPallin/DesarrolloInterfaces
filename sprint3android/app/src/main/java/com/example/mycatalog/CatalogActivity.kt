package com.example.mycatalog

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View

class CatalogActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_catalog)
        // Encuentra el botón por su ID
        val buttonToDetail = findViewById<View>(R.id.buttonToDetail)

        // Establece un OnClickListener para el botón
        buttonToDetail.setOnClickListener {
            // Crea una intención para iniciar la actividad DetailActivity
            val intent = Intent(this, DetailActivity::class.java)
            startActivity(intent)
        }
    }
}