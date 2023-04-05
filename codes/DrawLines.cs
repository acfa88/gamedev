using UnityEngine;

public class DrawLines : MonoBehaviour
{
    public float width;
    public List<Coordenadas> points = new List<Coordenadas>();

    void Start()
    {
        // Adiciona alguns pontos à lista com cores diferentes
        points.Add(new Coordenadas(transform.position.x, transform.position.y, Color.red));
        points.Add(new Coordenadas(1, 1, Color.green));
        points.Add(new Coordenadas(2, 2, Color.blue));
    }
    
    void Update()
    {
        // Desenha todos os pontos na lista
        foreach (Coordenadas point in points)
        {
            point.DrawPoint(width, point.color);
        }
    }
}
