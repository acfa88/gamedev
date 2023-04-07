using UnityEngine;

public class Coordinates
{
    private Vector3 _positionStart;
    private Vector3 _positionEnd;
    public Color color;

    // construtor com apenas a posição inicial
    public Coordinates(Vector3 positionStart, Color color)
    {
        _positionStart = positionStart;
        _positionEnd = positionStart;
        this.color = color;
    }

    // construtor com a posição inicial e final
    public Coordinates(Vector3 positionStart, Vector3 positionEnd, Color color)
    {
        _positionStart = positionStart;
        _positionEnd = positionEnd;
        this.color = color;
    }

    // sobrescrita do método ToString()
    public override string ToString()
    {
        return _positionStart.x + "," + _positionStart.y + "," + _positionStart.z + " - " + _positionEnd.x + "," + _positionEnd.y + "," + _positionEnd.z;
    }

    public void DrawPoint(float width, Color color)
    {      
        Vector3 position = new Vector3(_positionStart.x, _positionStart.y, _positionStart.z);        
        GameObject point = GameObject.CreatePrimitive(PrimitiveType.Sphere);
        point.transform.position = position;
        point.transform.localScale = new Vector3(width, width, width);
        point.GetComponent<MeshRenderer>().material.color = color;
    }

    public void DrawLine(float width, Color color)
    {
        GameObject line = new GameObject("Line");
        LineRenderer lineRenderer = line.AddComponent<LineRenderer>();
        lineRenderer.positionCount = 2;
        lineRenderer.SetPositions(new Vector3[] { _positionStart, _positionEnd });
        lineRenderer.startWidth = width/2;
        lineRenderer.endWidth = width/2;
        lineRenderer.material.color = color;
    }   
}