<script setup lang="ts">
import { onMounted, onUnmounted, reactive, ref } from 'vue'
import { Streamlit } from '~/stcomponentlib'
import { DsfrCheckbox } from '@gouvminint/vue-dsfr'

import { useStreamlit } from '../streamlit'
import type { ComponentProps } from '../types/ComponentProps'

useStreamlit()

const props = defineProps<
	ComponentProps<{
		modelValue?: boolean
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
const isFocused = ref(false)
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

const onRenderEvent = (_event: Event): void =>
	{
		if (!isFocused.value && checked.value)
		{
			checked.value = false
			Streamlit.setComponentValue(checked.value)
		}
	}

onMounted(() =>
	{
		Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRenderEvent)
	})

onUnmounted(() =>
	{
		Streamlit.events.removeEventListener(Streamlit.RENDER_EVENT, onRenderEvent)
	})

const onInput = (event: InputEvent) =>
	{
		event.preventDefault()
		checked.value = (event.target as HTMLInputElement).checked
		Streamlit.setComponentValue(checked.value)
	}

const onFocus = () =>
	{
		isFocused.value = true
	}

const onBlur = () =>
	{
		isFocused.value = false
	}
</script>

<template>
	<div class="component" :style="style">
		<DsfrCheckbox
			v-bind="props.args"
			v-model="checked"
			@input="onInput"
			@focus="onFocus"
			@blur="onBlur"
		/>
	</div>
</template>
