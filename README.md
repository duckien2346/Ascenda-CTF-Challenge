
# Assignment: Cloud Security Challenge

It is really a great pleasure to have a chance on this challenge to learn more about cloud security.
Thank you Ascenda Loyalty for providing a lesson through this challenge.

## Solution

The solution is based on [https://loyalty.dev/posts/rails-to-the-cloud](https://loyalty.dev/posts/rails-to-the-cloud) written by **Rouvin Erh**

The key idea is from this line of code in `pages_controller.rb`:

```ruby
    image = (anya_path + params.fetch(:img, 'anya.png')).gsub("../", "")
    file = File.open(image)
```

Even though, using `gsub("../", "")` to prevent Path Traversal, it is still possible to access the parent directory by using `....//` instead of `../`.


## Challenge Overview

repo: [https://github.com/Kaligo/hello-anya](https://github.com/Kaligo/hello-anya)

Your mission is to interact and try to exploit a cloud-hosted website to uncover a secret key hidden in a file within the website’s file system.

You are provided with the following resources:

- A cloud-hosted website: [https://hello-anya.fly.dev](https://hello-anya.fly.dev)
- The name of the text file that holds the secret key: **"secret_file"**
- The source code of the above website (the actual "secret_file" is not included)
- The first three letters of the secret: **"19b"**

