package cmd

import (
	"fmt"
	"io"
	"os"

	"github.com/spf13/cobra"
)

func init() {
	rootCmd.AddCommand(dayCmd)
}

var dayCmd = &cobra.Command{
	Use:   "day",
	Short: "Create a new day file",
	Args:  cobra.MatchAll(cobra.ExactArgs(1), cobra.OnlyValidArgs),
	Run: func(cmd *cobra.Command, args []string) {
		day := args[0]
		dest := cfg.Year + "/" + cfg.Language + "/"

		err := os.MkdirAll(dest, os.ModePerm)
		if err != nil {
			fmt.Printf("Error creating directory %q: %v\n", dest, err)
			return
		}

		src := "templates/template"
		switch cfg.Language {
		// ex: dest = 2024/python/day1.py
		case "python":
			dest += "day" + day + ".py"
			src += ".py"
		}

		_, err = os.Stat(dest)
		if !os.IsNotExist(err) {
			fmt.Printf("File %q already exists.\n", dest)
			return
		}

		template, err := os.Open(src)
		if err != nil {
			fmt.Printf("Error opening template file %q: %v\n", src, err)
			return
		}
		defer template.Close()

		f, err := os.Create(dest)
		if err != nil {
			fmt.Printf("Error creating new file %q: %v\n", dest, err)
			return
		}
		defer f.Close()

		_, err = io.Copy(f, template)
		if err != nil {
			fmt.Printf("Error copying template file contents: %v\n", err)
			return
		}

		fmt.Printf("Created new file %q\n", dest)
	},
}
