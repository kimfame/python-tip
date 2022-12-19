# 1. ECS Task의 IAM Role에 SSM Messages 권한이 있어야함

# 2. AWS CLI로 Container 접속 설정을 위한 Token 입력
aws configure

# 3. ECS Service에 execute command enable 설정
aws ecs update-service \
    --cluster blackturtle-dev-cluster \
    --service blackturtle-dev-api-service \
    --region ap-northeast-2 \
    --enable-execute-command > /dev/null

# 4. 재배포

# 5. enableExecuteCommand 값이 True인지 확인
# --tasks abcdefghiRUN <- task ID 복붙할 때, RUN 빼야됨
aws ecs describe-tasks \
    --cluster blackturtle-dev-cluster \
    --tasks 9c34cd4d0b6b4aa79fb64339fe60d724 | grep enableExecuteCommand

# 6. managedAgents running 확인
aws ecs describe-tasks \
    --cluster blackturtle-dev-cluster \
    --tasks 9c34cd4d0b6b4aa79fb64339fe60d724 | grep managedAgents --after-context=5

# 7. ECS Container에 접속 (Nginx)
aws ecs execute-command \
    --cluster blackturtle-dev-cluster \
    --task 9c34cd4d0b6b4aa79fb64339fe60d724 \
    --container blackturtle-dev-nginx \
    --interactive \
    --command "/bin/sh"

# 7. ECS Container에 접속 (App)
aws ecs execute-command \
    --cluster blackturtle-dev-cluster \
    --task 9c34cd4d0b6b4aa79fb64339fe60d724 \
    --container blackturtle-dev-app \
    --interactive \
    --command "/bin/sh"