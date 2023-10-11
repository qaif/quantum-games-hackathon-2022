using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.InputSystem;
using UnityEngine.SceneManagement;

public class Player : MonoBehaviour
{
    public Animator animator;
    public float speed = 2f;
    public EntanglementPopup entanglementPopup;
    private Vector2 moveDirection;
    private Measurement currentCollider = null;
    private EntanglementRoom currentEntanglementRoom = null;
    private WinLevel winLevel = null;
    private bool locked = false;

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
        if (!locked)
        {
            transform.position += new Vector3(moveDirection.x, moveDirection.y, 0) * Time.fixedDeltaTime * speed;
        }
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

    IEnumerator Interact()
    {
        yield return new WaitForSeconds(0.5f);
        if (currentCollider != null)
        {
            currentCollider.CollapseTrees();
        }
        if (currentEntanglementRoom != null)
        {
            entanglementPopup.SetupPopup(currentEntanglementRoom);
            // locked = true;
        }
        if (winLevel != null)
        {
            winLevel.Activate();
        }
    }

    public void OnInteract()
    {
        animator.SetTrigger("Interact");
        StartCoroutine(Interact());
    }

    public void OnEscape()
    {
        locked = false;
        entanglementPopup.ClosePopup();
    }

    IEnumerator Restart()
    {
        yield return new WaitForSeconds(1.5f);
        SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex);
    }

    public void OnRestart()
    {
        animator.SetTrigger("Die");
        locked = true;
        StartCoroutine(Restart());
    }

    void OnTriggerEnter2D(Collider2D col)
    {
        currentCollider = col.GetComponent<Measurement>();
        if (currentCollider != null)
        {
            currentCollider.stateToMeasure.ShowGlow();
        }
        currentEntanglementRoom = col.GetComponent<EntanglementRoom>();
        winLevel = col.GetComponent<WinLevel>();
    }

    void OnTriggerExit2D(Collider2D col)
    {
        if (currentCollider != null)
        {
            currentCollider.stateToMeasure.HideGlow();
        }
        currentCollider = null;
        currentEntanglementRoom = null;
        winLevel = null;
    }
}
