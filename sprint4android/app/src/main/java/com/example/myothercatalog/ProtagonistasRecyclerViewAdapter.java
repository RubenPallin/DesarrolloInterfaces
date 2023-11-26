package com.example.myothercatalog;

import android.app.Activity;
import android.content.Intent;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.List;

public class ProtagonistasRecyclerViewAdapter extends RecyclerView.Adapter<ProtagonistasViewHolder> {

    private List<ProtagonistasData> allTheData;
    private Activity activity;
    private Select_Listener select_listener;

    public ProtagonistasRecyclerViewAdapter(List<ProtagonistasData> allTheData, Activity activity, Select_Listener listener) {
        this.allTheData = allTheData;
        this.activity = activity;
        this.select_listener = listener;
    }

    @NonNull
    @Override
    public ProtagonistasViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext())
                .inflate(R.layout.protagonistas_view_holder, parent, false);
        return new ProtagonistasViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull ProtagonistasViewHolder holder, int position) {
        ProtagonistasData dataInPositionToBeRendered = allTheData.get(position);
        holder.showData(dataInPositionToBeRendered, activity);

        holder.itemView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                select_listener.onItemClick(dataInPositionToBeRendered);
            }
        });
    }

    @Override
    public int getItemCount() {
        return allTheData.size();
    }
}
