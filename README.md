# Tmux Setup

This repository contains my custom tmux setup. Follow the instructions below to install and configure it on your system.

## Installation on linux

~~~sh
git clone https://github.com/johansolbakken/johsoltmux.git "${XDG_CONFIG_HOME:-$HOME/.config}"/tmux
~~~

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

3. **Create Symlink (Optional)**

   You may want to create a symlink to make it easier to use the tmux configuration. Run:

   ```sh
   ln -s ~/.config/tmux/.tmux.conf ~/.tmux.conf
   ```

4. **Reload tmux Configuration**

   To apply the new configuration, reload tmux:

   ```sh
   tmux source-file ~/.tmux.conf
   ```

## Customization

You can customize the tmux configuration by editing the files in `~/.config/tmux`.

## Troubleshooting

If you encounter any issues or have questions, feel free to open an issue on the GitHub repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to replace `https://github.com/your-username/tmux-setup.git` with the actual URL of your repository.
