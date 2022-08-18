using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GroundFall : MonoBehaviour
{
    private Rigidbody rb;

    private void Start()
    {
        rb = GetComponent<Rigidbody>();

    }

  public IEnumerator SetRigitbodyValue()
    {
        yield return new WaitForSeconds(0.75f);
        rb.isKinematic = false;
        rb.useGravity = true;

    }
}
