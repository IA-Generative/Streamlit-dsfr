<script setup lang="ts">
import { reactive, ref, watch } from 'vue'
import { Streamlit } from '~/stcomponentlib'
import { DsfrCheckbox } from '@gouvminint/vue-dsfr'

import { useStreamlit } from '../streamlit'
import type { ComponentProps } from '../types/ComponentProps'

useStreamlit()

const props = defineProps<
	ComponentProps<{
		movelValue?: boolean
		required?: boolean
		small?: boolean
		name?: string
		hint?: string
		id?: string
		inline?: boolean
		errorMessage?: string
		validMessage?: string
	}>
>()

const checked = ref(false)
const style = reactive<{ [key: string]: string }>({})

if (props.theme)
{
	style['--base'] = props.theme.base
	style['--primary-color'] = props.theme.primaryColor
	style['--background-color'] = props.theme.backgroundColor
	style['--secondary-background-color'] = props.theme.secondaryBackgroundColor
	style['--text-color'] = props.theme.textColor
	style['--font'] = props.theme.font
}

watch(
	() => checked,
	(value) =>
		{
			Streamlit.setComponentValue(value)
		},
	{ immediate: true },
)
</script>

<template>
	<div class="component" :style="style">
		<DsfrCheckbox v-bind="props.args" v-model="checked" />
	</div>
</template>
