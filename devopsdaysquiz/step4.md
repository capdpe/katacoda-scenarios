a) Create a deployment called `cka3` that uses `busybox` as an **init container** to write the hostname of that **pod** to a file in a non-persistent volume. Then mount this file in a nginx:latest container at `/usr/share/nginx/html/index.html`

b) Expose the **deployment** using a service.

c) Scale up the service to 5 tracking all changes.

d) Use a `busybox:latest` pod to do a **nslookup** of the service using its DNS entry and write the outputs to a file = q4.txt
