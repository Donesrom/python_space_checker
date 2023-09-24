import psutil

def get_free_space():
  """Gets the free disk space on the persistent storage.

  Returns:
    The free disk space in GB.
  """

  root_partition = "/"
  usage = psutil.disk_usage(root_partition)

  free_space = usage.free / (1024 ** 3)

  return free_space

def main():
  # The main function.
  threshold = 70
  free_space = get_free_space()

  # Print the value of the free_space and threshold variables.
  print("Free disk space:", free_space)
  print("Threshold:", threshold)

  # Check if the free disk space is less than the threshold.
#  if free_space < threshold:
 #   message = "Warning: Free disk space is less than {} GB".format(threshold)
   # Send the Slack alert.
    #send_slack_alert(message)

if __name__ == "__main__":
  main()

