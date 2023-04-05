using System.Collections;
using System.Collections.Generic;
using UnityEngine;
/*
Pra fazer um personagem se movimentar em uma plataforma em Unity, 
você pode usar o componente "CharacterController" e o método "Move()".
Veja um exemplo de como o código pode ficar:
*/
public class CharacterMovement : MonoBehaviour
{
    public float speed = 5f;
    public float jumpForce = 10f;
    public float raycastDistance = 0.1f;

    private Rigidbody2D rb;
    private bool isGrounded;

    void Start()
    {
        rb = GetComponent<Rigidbody2D>();
    }

    void Update()
    {
        float x = Input.GetAxis("Horizontal");

        rb.velocity = new Vector2(x * speed, rb.velocity.y);

        if (Input.GetButtonDown("Jump") && isGrounded)
        {
            rb.AddForce(new Vector2(0, jumpForce), ForceMode2D.Impulse);
        }

        /*
        Este script faz o personagem se movimentar para a direita ou para a esquerda com as teclas de seta horizontal
        e pulando com a barra de espaço.
        É importante notar que o personagem só poderá pular se estiver tocando no chão (para isso,
        foi adicionado o código para detectar colisões com um objeto com a tag "Ground").
        Lembre-se de adicionar o componente Rigidbody2D ao seu personagem e de configurar os inputs na Unity. 
        Além disso, você pode querer adicionar um sprite para o personagem e um sprite para o chão,
        para que você possa ver o jogo em ação.
        */

        /*
        Para fazer o sprite do personagem girar quando ele virar para a direita ou para a esquerda,
        basta adicionar o seguinte código no script:
        */

        if (x > 0)
        {
            transform.localScale = new Vector3(1, 1, 1);
        }
        else if (x < 0)
        {
            transform.localScale = new Vector3(-1, 1, 1);
        }

        /*
        Este código verifica se o personagem está se movendo para a direita (x > 0) ou para a esquerda (x < 0) e,
        em seguida, altera a escala local do personagem para girar o sprite. 
        A escala local é um vetor que representa a escala do objeto em cada um dos eixos (x, y, z).
        Ao alterar o valor do eixo x para 1 ou -1, o sprite do personagem é girado.        
        */

        CheckGround();
    }

    void CheckGround()
    {
        RaycastHit2D hit = Physics2D.Raycast(transform.position, Vector2.down, raycastDistance);
        if (hit.collider != null)
        {
            if (hit.collider.tag == "Ground")
            {
                isGrounded = true;
            }
        }
        else
        {
            isGrounded = false;
        }
    }
}

/*
Este código usa o método "Raycast" para enviar um raio a partir da posição atual do personagem na direção para baixo (Vector2.down).
 Se o raio colidir com algum objeto, o método retorna um objeto "RaycastHit2D" com informações sobre a colisão. 
 Se o objeto colidido tiver a tag "Ground", a variável "isGrounded" é configurada como true, 
 indicando que o personagem está no chão.
Se o raio não colidir com nenhum objeto, "isGrounded" é configurado como false.
Lembre-se de adicionar uma tag "Ground" ao objeto que você quer que seja considerado como chão pelo personagem. 
Você também pode alterar a distância do raio usando a variável "raycastDistance".
*/

    /*
        void OnCollisionEnter2D(Collision2D collision)
    {
        if (collision.gameObject.tag == "Ground")
        {
            isGrounded = true;
        }
    }
    
    void OnCollisionExit2D(Collision2D collision)
    {
        if (collision.gameObject.tag == "Ground")
        {
            isGrounded = false;
        }
    }
    */
