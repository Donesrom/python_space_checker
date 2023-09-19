import psutil

def check_disk_space(min_threshold_gb=10):
    root_partition = "/var/lib/data" #should be on the persistent storage
    usage = psutil.disk_usage(root_partition)

    # Convert bytes to gigabytes
    total_gb = usage.total / (1024 ** 3)
    used_gb = usage.used / (1024 ** 3)
    free_gb = usage.free / (1024 ** 3)

    # Check if free space is below the minimum threshold
    if free_gb < min_threshold_gb:
        print(f"Warning: Disk space on '{root_partition}' is below {min_threshold_gb} GB.")
        print(f"Total space: {total_gb:.2f} GB")
        print(f"Used space: {used_gb:.2f} GB")
        print(f"Free space: {free_gb:.2f} GB")
    else:
        print(f"Disk space on '{root_partition}' is sufficient.")
        print(f"Total space: {total_gb:.2f} GB")
        print(f"Used space: {used_gb:.2f} GB")
        print(f"Free space: {free_gb:.2f} GB")

if __name__ == "__main__":
    threshold = 70  # Set your desired minimum threshold in GB
    check_disk_space(threshold)
