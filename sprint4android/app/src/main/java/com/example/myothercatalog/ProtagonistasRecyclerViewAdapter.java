package com.example.myothercatalog;

import android.app.Activity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.List;

public class ProtagonistasRecyclerViewAdapter extends RecyclerView.Adapter<ProtagonistasViewHolder> {

    private List<ProtagonistasData> allTheData;
    private Activity activity;

    public ProtagonistasRecyclerViewAdapter(List<ProtagonistasData> dataSet, Activity activity){
        this.allTheData = dataSet;
        this.activity = activity;
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
    }

    @Override
    public int getItemCount() {
        return allTheData.size();
    }
}
