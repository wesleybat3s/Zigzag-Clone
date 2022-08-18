using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BallMove : MonoBehaviour
{
    [SerializeField] private BallTransmiter ballTransmiter;

    [SerializeReference] private float ballMoveSpeed;

    private void Update()
    {
        SetBallMove();
    }

    private void SetBallMove()
    {
        transform.position += ballTransmiter.GetBallDirection() * ballMoveSpeed * Time.deltaTime;
    }
}
