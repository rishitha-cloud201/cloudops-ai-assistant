# Troubleshooting Guide

## CrashLoopBackOff

A CrashLoopBackOff state usually means the container starts, fails, and repeatedly restarts.

Common causes:

- Missing environment variables
- Invalid application configuration
- Database connection failures
- Failed startup command
- Health check misconfiguration

## ImagePullBackOff

An ImagePullBackOff state means Kubernetes cannot pull the container image.

Common causes:

- Incorrect image name
- Wrong image tag
- Missing registry credentials
- Private image repository access issue

## Recommended Investigation Commands

```bash
kubectl get pods -n <namespace>
kubectl describe pod <pod-name> -n <namespace>
kubectl logs <pod-name> -n <namespace>
kubectl get events -n <namespace>
```
