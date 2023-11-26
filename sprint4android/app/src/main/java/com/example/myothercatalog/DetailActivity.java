package com.example.myothercatalog;

import android.content.Intent;
import android.os.Bundle;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import com.bumptech.glide.Glide;

public class DetailActivity extends AppCompatActivity {

    public static final String EXTRA_NAME = "extra_name";
    public static final String TITLE = "TITLE" ;
    public static final String URL = "URL" ;
    public static final String DESCRIPTION = "DESCRIPTION" ;
    private String url;
    private String description;
    private String title;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_detail);
        ImageView image = findViewById(R.id.imageview_detail_activity);
        TextView title_detail = findViewById(R.id.textTitle);
        TextView description_detail = findViewById(R.id.descriptionText);


        Intent intent = getIntent();

        title = intent.getStringExtra(TITLE);
        description = intent.getStringExtra(DESCRIPTION);
        url = intent.getStringExtra(URL);

        Glide.with(DetailActivity.this).load(url).into(image);
        title_detail.setText(title);
        description_detail.setText(description);
    }
}
