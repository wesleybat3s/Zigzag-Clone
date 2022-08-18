using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GroundPosition : MonoBehaviour
{
    private GroundSpawner groundSpawner;
    
    private Rigidbody rb;
    
    [SerializeField] private float endYValue;

    private int groundDirection;

    private void Start()
    {
        groundSpawner = FindObjectOfType<GroundSpawner>();

        rb = GetComponent<Rigidbody>();
        
    }

    private void Update()
    {
        CheckGroundYPosition();
    }

    private void CheckGroundYPosition()
    {
        if (transform.position.y <= endYValue)
        {
            SetRigitbodyValue();
            SetGroundNewPosiiton();          
        }
    }

    private void SetGroundNewPosiiton()
    {
        groundDirection = Random.Range(0, 2);

        if (groundDirection == 0)
        {
            transform.position = new Vector3(groundSpawner.lastGroundObject.transform.position.x - 1f, groundSpawner.lastGroundObject.transform.position.y, groundSpawner.lastGroundObject.transform.position.z);
        }

        else
        {
            transform.position = new Vector3(groundSpawner.lastGroundObject.transform.position.x, groundSpawner.lastGroundObject.transform.position.y, groundSpawner.lastGroundObject.transform.position.z + 1f);
        }

        groundSpawner.lastGroundObject = gameObject;
    }

    private void SetRigitbodyValue()
    {
        rb.isKinematic = true;
        rb.useGravity = false;
    }

}
