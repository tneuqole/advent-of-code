package cmd

import (
	"fmt"
	"os"
	"strconv"
	"time"

	"github.com/go-playground/validator/v10"
	"github.com/spf13/cobra"
	"github.com/spf13/viper"
)

type Config struct {
	Year     string `json:"year" validate:"validateYear"`
	Language string `json:"language" validate:"oneof=python"`
}

func validateYear(fl validator.FieldLevel) bool {
	year, err := time.Parse("2006", fl.Field().String())
	if err != nil {
		return false
	}
	return 2015 <= year.Year() && year.Year() <= time.Now().Year()
}

func validateConfig() {
	viper.Unmarshal(&cfg)
	v := validator.New()
	v.RegisterValidation("validateYear", validateYear)
	if err := v.Struct(cfg); err != nil {
		panic(err)
	}
}

var (
	cfg Config

	rootCmd = &cobra.Command{
		Use:   "aoc",
		Short: "Quickly create new files for Advent of Code problems",
		Run:   func(cmd *cobra.Command, args []string) {},
	}
)

func Execute() {
	err := rootCmd.Execute()
	if err != nil {
		os.Exit(1)
	}
}

func init() {
	cobra.OnInitialize(initConfig)
}

func initConfig() {
	viper.SetDefault("year", strconv.Itoa(time.Now().Year()))
	viper.SetDefault("language", "python")

	viper.SetConfigFile("./config.json")
	if err := viper.ReadInConfig(); err == nil {
		fmt.Println("Using config file:", viper.ConfigFileUsed())
	}

	validateConfig()

	fmt.Printf("config=%+v\n", cfg)
}
