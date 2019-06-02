action "Hello World" {
  uses = "./my-action"
  env = {
    FIRST_NAME  = "Mona"
    MIDDLE_NAME = "Lisa"
    LAST_NAME   = "Octocat"
  }
}
