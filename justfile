build-rpm:
  #!/bin/bash
  podman run --rm --cap-add=SYS_ADMIN --privileged --volume ./:/anda --volume mock_cache:/var/lib/mock --workdir /anda ghcr.io/terrapkg/builder:f43 anda \
      build -c fedora-43-x86_64 pkgs/aerothemeplasma-icons/pkg
