using UnityEngine;

public class Coordinates
{
    private Vector3 _position;
    public Color color;

    // construtor
    public Coordinates(Vector3 position, Color color)
    {
        _position = position;
        this.color = color;
    }

    // sobrescrita do método ToString()
    public override string ToString()
    {
        return _position.x + "," + _position.y + "," + _position.z;
    }
    
    public void DrawPoint(float width, Color color)
    {      
        Vector3 position = new Vector3(_position.x, _position.y, _position.z);        
        GameObject point = GameObject.CreatePrimitive(PrimitiveType.Sphere);
        point.transform.position = position;
        point.transform.localScale = new Vector3(width, width, width);
        point.GetComponent<MeshRenderer>().material.color = color;
    }
}
