package cmd

import (
	"github.com/spf13/cobra"
	"github.com/spf13/viper"
)

var (
	year     string
	language string

	setCmd = &cobra.Command{
		Use:   "set",
		Short: "Set year and language",
		Run: func(cmd *cobra.Command, args []string) {
			if year != "" {
				viper.Set("year", year)
			}
			if language != "" {
				viper.Set("language", language)
			}

			validateConfig()
			err := viper.WriteConfig()
			if err != nil {
				panic(err)
			}
		},
	}
)

func init() {
	rootCmd.AddCommand(setCmd)

	setCmd.Flags().StringVarP(&year, "year", "y", "", "Configure the year")
	setCmd.Flags().StringVarP(&language, "language", "l", "", "Configure the programming language")
}
