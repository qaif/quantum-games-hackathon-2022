using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.InputSystem;

public class Player : MonoBehaviour
{
    public Animator animator;
    public float speed = 2f;
    private Vector2 moveDirection;
    private QuantumState currentCollider = null;

    // Start is called before the first frame update
    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {

    }

    void FixedUpdate()
    {
        transform.position += new Vector3(moveDirection.x, moveDirection.y, 0) * Time.fixedDeltaTime * speed;
    }


    public void OnMove(InputValue value)
    {
        moveDirection = value.Get<Vector2>();

        float deltaInputs = Mathf.Abs(moveDirection.x) - Mathf.Abs(moveDirection.y);

        if (deltaInputs > 0f)
        {
            moveDirection.y = 0f;
        }
        else
        {
            moveDirection.x = 0f;
        }

        if (moveDirection != Vector2.zero)
        {
            animator.SetFloat("XInput", moveDirection.x);
            animator.SetFloat("YInput", moveDirection.y);
            animator.SetBool("IsWalking", true);
        }
        else
        {
            animator.SetBool("IsWalking", false);
        }
    }

    public void OnInteract()
    {
        if (currentCollider != null)
        {
            currentCollider.CollapseTrees();
        }
    }

    void OnTriggerEnter2D(Collider2D col)
    {
        currentCollider = col.GetComponent<QuantumState>();
    }

    void OnTriggerExit2D(Collider2D col)
    {
        currentCollider = null;
    }
}
