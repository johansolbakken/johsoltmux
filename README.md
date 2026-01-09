# Tmux Setup

This repository contains my custom tmux setup. Follow the instructions below to install and configure it on your system.

## Installation on Linux

1. **Clone the Repository**

   ```sh
   git clone https://github.com/johansolbakken/johsoltmux.git "${XDG_CONFIG_HOME:-$HOME/.config}"/tmux
   ```

2. **Install tmux** (if not already installed)

   ```sh
   # Ubuntu/Debian
   sudo apt install tmux

   # Fedora
   sudo dnf install tmux

   # Arch
   sudo pacman -S tmux
   ```

3. **Install TPM and Plugins**

   Start tmux and install the plugins:

   ```sh
   tmux
   ```

   Then press `Ctrl-Space` + `I` (capital i) to install the plugins via TPM.

## Installation on macOS

1. **Clone the Repository**

   Open your terminal and run the following command to clone the repository. The repository will be cloned into `~/.config/tmux`.

   ```sh
   git clone https://github.com/johansolbakken/johsoltmux.git ~/.config/tmux
   ```

2. **Install tmux**

   If you haven't already installed tmux, you can do so using Homebrew:

   ```sh
   brew install tmux
   ```

3. **Install TPM and Plugins**

   Start tmux and install the plugins:

   ```sh
   tmux
   ```

   Then press `Ctrl-Space` + `I` (capital i) to install the plugins via TPM.

4. **Reload tmux Configuration (Optional)**

   If you're already in a tmux session, reload the configuration:

   ```sh
   tmux source-file ~/.config/tmux/tmux.conf
   ```

   Or inside tmux: `Ctrl-Space` + `r`

## Customization

You can customize the tmux configuration by editing the files in `~/.config/tmux`.

## Troubleshooting

If you encounter any issues or have questions, feel free to open an issue on the GitHub repository.

## Features

- **Prefix:** `Ctrl-Space` (more ergonomic than default `Ctrl-b`)
- **Navigation:** Arrow keys for pane navigation (both with and without prefix)
- **Vim integration:** Seamless navigation between Vim and tmux panes
- **Copy mode:** Vim-style selection with `v` and `y` for yank
- **Mouse support:** Enabled for easy pane resizing and selection
- **Minimal theme:** Clean status bar with green accents
- **Truecolor support:** Full RGB color support for modern terminal themes

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
