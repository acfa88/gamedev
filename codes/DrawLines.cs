using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DrawLines : MonoBehaviour
{
    public float width;
    public List<Coordinates> points = new List<Coordinates>();

    void Start()
    {
        // Adiciona alguns pontos à lista com cores diferentes
        points.Add(new Coordinates(new Vector3(transform.position.x, transform.position.y, 0), Color.red));
        points.Add(new Coordinates(new Vector3(1, 1, 0), Color.green));
        points.Add(new Coordinates(new Vector3(2, 2, 0), Color.blue));

        // Desenha todos os pontos na lista
        foreach (Coordinates point in points)
        {
            point.DrawPoint(width, point.color);
        }
    }    

}
