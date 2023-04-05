using UnityEngine;

public class Coordenadas
{
    private float _X;
    private float _Y;
    private float _Z;
    public Color color;

    // construtor
    public Coordenadas(float x, float y, Color color)
    {
        _X = x;
        _Y = y;
        _Z = -1;
        this.color = color;
    }

    // sobrescrita do método ToString()
    public override string ToString()
    {
        return _X + "," + _Y + "," + _Z;
    }

    public void DrawPoint(float width, Color color)
    {      
        Vector3 position = new Vector3(_X, _Y, _Z);
        GameObject point = new GameObject("Point");
        LineRenderer lineRenderer = point.AddComponent<LineRenderer>();
        lineRenderer.positionCount = 1;
        lineRenderer.SetPosition(0, position);
        lineRenderer.startWidth = width;
        lineRenderer.endWidth = width;
        lineRenderer.material.color = color;
    }
}


