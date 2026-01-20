variable "aws_region" {
  description = "AWS region for resources"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Project name for resource naming"
  type        = string
  default     = "secure-cicd-pipeline"
}

variable "environment" {
  description = "Environment name"
  type        = string
  default     = "dev"
}

variable "vpc_cidr" {
  description = "CIDR block for VPC"
  type        = string
  default     = "10.0.0.0/16"
}

variable "availability_zones" {
  description = "Availability zones for subnets"
  type        = list(string)
  default     = ["us-east-1a", "us-east-1b"]
}

variable "public_subnet_cidrs" {
  description = "CIDR blocks for public subnets"
  type        = list(string)
  default     = ["10.0.1.0/24", "10.0.2.0/24"]
}

variable "private_subnet_cidrs" {
  description = "CIDR blocks for private subnets"
  type        = list(string)
  default     = ["10.0.11.0/24", "10.0.12.0/24"]
}

variable "app_port" {
  description = "Port the application listens on"
  type        = number
  default     = 8080
}

variable "app_count" {
  description = "Number of application instances"
  type        = number
  default     = 2
}

variable "fargate_cpu" {
  description = "Fargate instance CPU units (1024 = 1 vCPU)"
  type        = number
  default     = 256
}

variable "fargate_memory" {
  description = "Fargate instance memory in MB"
  type        = number
  default     = 512
}

variable "health_check_path" {
  description = "Health check endpoint path"
  type        = string
  default     = "/health"
}

variable "container_image" {
  description = "Container image to deploy"
  type        = string
  default     = "latest"
}